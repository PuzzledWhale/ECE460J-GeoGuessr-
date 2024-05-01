import pyautogui
import torch
import clip
import os
from PIL import Image
from pynput import keyboard

def crop_center(image, crop_width, crop_height):
    width, height = image.size
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = (width + crop_width) // 2
    bottom = (height + crop_height) // 2
    return image.crop((left, top, right, bottom))

print('preparing model...')

class_names = os.listdir('data/archive/compressed_dataset/')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model, preprocess = clip.load("ViT-B/32", device=device, jit=False)

model.load_state_dict(torch.load("models/20240429-134354_model.pt", map_location=device))
model = model.to(device)

model.eval()
text_inputs = torch.cat([clip.tokenize(f'{c}') for c in class_names]).to(device)

print('model is ready! Press the n key to take a screenshot and feed it into the model! Press any other button to close (crash) this program')

def on_press(key):
    if key.char == 'n':
        print("\nScreenshotted! Feeding image into model...")
        image = pyautogui.screenshot()
        image = crop_center(image, 1536, 662)
        image.save('cropped.png') # use this if you want to see the screenshot that is being fed into the model
        image_input = preprocess(image).unsqueeze(0).to(device)

        with torch.no_grad():
            image_features = model.encode_image(image_input)
            text_features = model.encode_text(text_inputs)

        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
        values, indices = similarity[0].topk(5)

        print("Top prediction(s):")
        for value, index in zip(values, indices):
            print(f"{class_names[index]}: {100*value.item():.2f}%")
    else:
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()