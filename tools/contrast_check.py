import re
import sys
from pathlib import Path

SCSS = Path(r"c:\Users\Will_\Documents\GitHub\ramblings\_sass\_minimalistic.scss").read_text()
# find CSS vars
vars = dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{3,6})", SCSS))

# helpers

def hex_to_rgb(h):
    h = h.lstrip('#')
    if len(h) == 3:
        h = ''.join(ch*2 for ch in h)
    return tuple(int(h[i:i+2], 16) for i in (0,2,4))


def srgb_to_lin(c):
    c = c/255.0
    return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055) ** 2.4


def rel_lum(rgb):
    r,g,b = [srgb_to_lin(v) for v in rgb]
    return 0.2126*r + 0.7152*g + 0.0722*b


def contrast_ratio(hex1, hex2):
    l1 = rel_lum(hex_to_rgb(hex1))
    l2 = rel_lum(hex_to_rgb(hex2))
    lighter = max(l1,l2)
    darker = min(l1,l2)
    return (lighter+0.05)/(darker+0.05)

# pairs to check
pairs = [
    ("text-primary","bg-primary"),
    ("text-secondary","bg-primary"),
    ("accent","bg-primary"),
    ("button-text","button-bg"),
    ("text-primary","code-bg"),
]

print("Found variables:")
for k in sorted(vars):
    print(f"  --{k}: {vars[k]}")

print('\nContrast checks:')
for a,b in pairs:
    if a in vars and b in vars:
        r = contrast_ratio(vars[a], vars[b])
        pass_norm = r >= 4.5
        pass_large = r >= 3.0
        print(f"  {a} ({vars[a]}) on {b} ({vars[b]}) -> {r:.2f}: {'AA' if pass_norm else 'FAIL'} (large {'OK' if pass_large else 'FAIL'})")
    else:
        print(f"  missing vars for {a} or {b}")

# estimate characters per line
max_width_px_match = re.search(r"max-width:\s*(\d+)px", SCSS)
max_width_ch_match = re.search(r"max-width:\s*(\d+)ch", SCSS)
if max_width_px_match:
    max_w_px = int(max_width_px_match.group(1))
    # approximate characters per line assuming avg char width ~0.5em and 16px base
    font_size_match = re.search(r"font-size:\s*(\d+)px", SCSS)
    font_size = int(font_size_match.group(1)) if font_size_match else 16
    chars = max_w_px / (font_size * 0.5)
    print(f"\nLayout estimate: max-width = {max_w_px}px, font-size ≈ {font_size}px -> approx {chars:.0f} characters per line")
elif max_width_ch_match:
    ch_count = int(max_width_ch_match.group(1))
    chars = ch_count
    print(f"\nLayout estimate: max-width = {ch_count}ch -> approx {ch_count} characters per line")
else:
    # fallback
    max_w = 820
    font_size_match = re.search(r"font-size:\s*(\d+)px", SCSS)
    font_size = int(font_size_match.group(1)) if font_size_match else 16
    chars = max_w / (font_size * 0.5)
    print(f"\nLayout estimate: max-width = {max_w}px (default), font-size ≈ {font_size}px -> approx {chars:.0f} characters per line")

# suggestions
print('\nSuggestions:')
if vars.get('text-primary') and vars.get('bg-primary'):
    r = contrast_ratio(vars['text-primary'], vars['bg-primary'])
    if r < 4.5:
        print(f"  - text contrast is {r:.2f}: consider lightening text or darkening background to reach >=4.5:1")
    else:
        print(f"  - text contrast {r:.2f} passes AA for normal text.")

if chars > 80:
    print(f"  - Lines are long (~{chars:.0f} chars). Consider reducing max-width to 68ch or ~680px for 16px base to target 68 characters per line.")
else:
    print(f"  - Line length (~{chars:.0f} chars) is within a comfortable range.")

print('\nDone.')
