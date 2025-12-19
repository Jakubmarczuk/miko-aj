from PIL import Image, ImageDraw, ImageFilter

def draw_santa(size=800, scale=3, save_path="santa.png"):
    W = H = size * scale
    center_x = W // 2
    center_y = H // 2

    bg_color = (20, 40, 80)
    skin = (241, 194, 125)
    red = (200, 20, 40)
    white = (255, 255, 255)
    black = (20, 20, 20)
    belt = (20, 20, 20)
    gold = (212, 175, 55)

    img = Image.new("RGB", (W, H), bg_color)
    draw = ImageDraw.Draw(img)

    head_r = int(0.25 * W)
    head_x0 = center_x - head_r
    head_y0 = center_y - head_r
    head_x1 = center_x + head_r
    head_y1 = center_y + head_r

    torso_w = int(0.9 * W)
    torso_h = int(0.5 * H)
    torso_x0 = center_x - torso_w // 2
    torso_y0 = head_y1 - int(0.08 * W)
    torso_x1 = torso_x0 + torso_w
    torso_y1 = torso_y0 + torso_h

    draw.rectangle([torso_x0, torso_y0, torso_x1, torso_y1], fill=red)

    belt_h = int(0.06 * H)
    belt_y0 = torso_y0 + torso_h // 3
    draw.rectangle([torso_x0, belt_y0, torso_x1, belt_y0 + belt_h], fill=belt)
    buckle_w = int(0.12 * W)
    buckle_h = int(0.08 * H)
    buckle_x0 = center_x - buckle_w // 2
    buckle_y0 = belt_y0 + (belt_h - buckle_h) // 2
    draw.rectangle([buckle_x0, buckle_y0, buckle_x0 + buckle_w, buckle_y0 + buckle_h], fill=gold)

    draw.ellipse([head_x0, head_y0, head_x1, head_y1], fill=skin, outline=None)

    beard_top = head_y0 + int(0.45 * head_r)
    beard_bottom = head_y1 + int(0.5 * head_r)
    draw.ellipse([center_x - int(0.9 * head_r), beard_top, center_x + int(0.9 * head_r), beard_bottom], fill=white)

    moustache_y = head_y0 + int(0.55 * head_r)
    draw.ellipse([center_x - int(0.6 * head_r), moustache_y - int(0.05 * head_r),
                  center_x - int(0.05 * head_r), moustache_y + int(0.25 * head_r)], fill=white)
    draw.ellipse([center_x + int(0.05 * head_r), moustache_y - int(0.05 * head_r),
                  center_x + int(0.6 * head_r), moustache_y + int(0.25 * head_r)], fill=white)

    mouth_y = moustache_y + int(0.18 * head_r)
    draw.arc([center_x - int(0.18 * head_r), mouth_y, center_x + int(0.18 * head_r), mouth_y + int(0.12 * head_r)],
             start=0, end=180, fill=(140, 40, 40), width=int(max(1, scale)))

    nose_r = int(0.06 * W)
    nose_x0 = center_x - nose_r
    nose_y0 = head_y0 + int(0.43 * head_r)
    draw.ellipse([nose_x0, nose_y0, nose_x0 + 2 * nose_r, nose_y0 + 2 * nose_r], fill=(230, 110, 80))

    eye_r = int(0.04 * W)
    eye_y = head_y0 + int(0.28 * head_r)
    eye_dx = int(0.14 * head_r)
    draw.ellipse([center_x - eye_dx - eye_r, eye_y - eye_r, center_x - eye_dx + eye_r, eye_y + eye_r], fill=black)
    draw.ellipse([center_x + eye_dx - eye_r, eye_y - eye_r, center_x + eye_dx + eye_r, eye_y + eye_r], fill=black)
    highlight_r = max(1, int(0.01 * W))
    draw.ellipse([center_x - eye_dx - highlight_r, eye_y - eye_r + highlight_r, center_x - eye_dx + highlight_r,
                  eye_y - eye_r + 3 * highlight_r], fill=white)
    draw.ellipse([center_x + eye_dx - highlight_r, eye_y - eye_r + highlight_r, center_x + eye_dx + highlight_r,
                  eye_y - eye_r + 3 * highlight_r], fill=white)

    brow_w = int(0.12 * head_r)
    brow_h = max(1, int(0.02 * H))
    draw.rectangle([center_x - eye_dx - brow_w // 2, eye_y - int(0.2 * head_r) - brow_h,
                    center_x - eye_dx + brow_w // 2, eye_y - int(0.2 * head_r)], fill=(80, 40, 30))
    draw.rectangle([center_x + eye_dx - brow_w // 2, eye_y - int(0.2 * head_r) - brow_h,
                    center_x + eye_dx + brow_w // 2, eye_y - int(0.2 * head_r)], fill=(80, 40, 30))

    hat_top_x = center_x
    hat_top_y = head_y0 - int(0.6 * head_r)
    hat_left = center_x - int(0.95 * head_r)
    hat_right = center_x + int(0.95 * head_r)
    draw.polygon([(hat_top_x, hat_top_y), (hat_left, head_y0 + int(0.05 * head_r)), (hat_right, head_y0 + int(0.05 * head_r))], fill=red)
    brim_h = int(0.14 * head_r)
    draw.ellipse([hat_left, head_y0 - brim_h // 2, hat_right, head_y0 + brim_h], fill=white)

    pom_r = int(0.12 * head_r)
    draw.ellipse([hat_top_x - pom_r, hat_top_y - pom_r, hat_top_x + pom_r, hat_top_y + pom_r], fill=white)

    btn_r = int(0.035 * W)
    btn_x = center_x
    for i in range(3):
        y = torso_y0 + int(0.25 * torso_h) + i * int(0.18 * torso_h)
        draw.ellipse([btn_x - btn_r, y - btn_r, btn_x + btn_r, y + btn_r], fill=black)

    beard_box = (center_x - int(0.95 * head_r), moustache_y - int(0.2 * head_r),
                 center_x + int(0.95 * head_r), beard_bottom + int(0.05 * head_r))
    beard_region = img.crop(beard_box).filter(ImageFilter.GaussianBlur(radius=scale * 0.6))
    img.paste(beard_region, beard_box)

    final = img.resize((size, size), resample=Image.LANCZOS)
    final.save(save_path)
    return final

if __name__ == "__main__":
    out = draw_santa(size=800, scale=3, save_path="santa.png")
    try:
        out.show()
    except Exception:
        print("Obraz zapisany jako 'santa.png'. Otwórz go ręcznie jeśli nie otworzył się automatycznie.")
