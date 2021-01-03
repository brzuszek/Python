from PIL import Image
import glob

n=0
while n<4:
    new_img=Image.new("CMYK",(100,100),color="black")
    new_img.save("Newpic"+str(n)+".jpg")
    n=n+1

for picture in glob.glob("*.jpg"):
    img = Image.open(picture)
    rgb_img = img.convert('RGB')
    rgb_img.save(picture.replace("jpg", "png"))
