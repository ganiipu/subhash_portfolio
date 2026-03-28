import os
import shutil

brain = r"C:\Users\default.LAPTOP-UQP63FS1\.gemini\antigravity\brain\b6ed569b-95cb-481a-bc3b-c65d9cefdc8c"
dest  = r"c:\Users\default.LAPTOP-UQP63FS1\n8n\project portfolio\assets"

files = [
    ("llm_text_emotion_light_1774576759397.png", "llm1.png"),
    ("llm_fake_news_light_1774576773299.png",    "llm2.png"),
    ("llm_ner_light_1774576785955.png",          "llm3.png"),
    ("llm_vision_light_1774576801509.png",       "llm4.png"),
    ("llm_phi2_light_1774576815909.png",         "llm5.png"),
]

for src_name, dst_name in files:
    src = os.path.join(brain, src_name)
    dst = os.path.join(dest, dst_name)
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        print("Copied:", dst_name)
    else:
        print("MISSING:", src_name)

print("Done.")
