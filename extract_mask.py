from PIL import Image


def extract_mask(image_path, save_folder):
    # Open the image
    image = Image.open(image_path)

    # Check if the image has an alpha channel
    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
        # Extract the alpha channel
        alpha = image.getchannel('A')

        # Save the alpha channel (mask) to a given folder
        mask_file_name = 'hm.jpg'
        mask_save_path = f'{save_folder}/{mask_file_name}'
        alpha.save(mask_save_path)

        print(f'Mask saved to: {mask_save_path}')
    else:
        print("The image doesn't have an alpha channel.")


if __name__ == '__main__':
    image_name = input("Please enter the image file name (including the extension, e.g. 'image.png'): ")
    image_path = f'datasets/test/cloth/{image_name}'
    save_folder = 'datasets/test/cloth-mask'

    extract_mask(image_path, save_folder)
