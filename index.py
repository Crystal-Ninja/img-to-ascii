import PIL.Image
# ASCII_CHARS=["@","#","S","%","?","*","+",";",":",",","."]
ASCII_CHARS=[".",",",":",";","+","*","?","%","S","#","@"]

def resize_image(image,new_width=100,height_scale=0.55):
    width,height=image.size
    ratio=height/width
    new_height=int(new_width*ratio*height_scale)
    resized_image=image.resize((new_width,new_height))
    return(resized_image)

def graying(image):
    grayscale_img=image.convert("L")
    return(grayscale_img)

def pixelToAscii(image):
    pixels=image.getdata()
    characters="".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main(new_width=100):
    path=input("enter the valid path to the image:\n")
    try:
        image=PIL.Image.open(path)
    except:
        print(path,"is not a valid pathname to an image:\n")
    
    new_image=pixelToAscii(graying(resize_image(image)))

    pixel_count=len(new_image)
    ascii_image="\n".join(new_image[i:(i+new_width)] for i in range(0,pixel_count,new_width))

    print(ascii_image)

    with ("ascii_image.txt","w") as f:
        f.write(ascii_image)
main()