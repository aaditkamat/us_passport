# A Python script to convert a JPEG file to one that meets US Passport size photo requirements

from PIL import Image
import os

def create_passport_photo(input_path, output_path):
    """
    Convert an image to meet US Passport photo requirements:
    - Size: 2x2 inches (600x600 pixels at 300 DPI)
    - Head height: 1 inch to 1-3/8 inches (between 300-413 pixels)
    - Eye height position: 1-1/8 inches to 1-3/8 inches from bottom (338-413 pixels from bottom)
    - White background
    - Color photo
    
    Args:
        input_path (str): Path to input JPEG image
        output_path (str): Path to save the processed passport photo
    """
    
    # Open the image
    with Image.open(input_path) as img:
        # Convert to RGB if not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Create a white background of passport size
        passport_size = (600, 600)  # 2x2 inches at 300 DPI
        background = Image.new('RGB', passport_size, 'white')
        
        # Calculate resize ratio to fit height within passport requirements
        # Target height should be around 375 pixels (1.25 inches at 300 DPI)
        target_height = 375
        ratio = target_height / img.height
        new_width = int(img.width * ratio)
        new_height = target_height
        
        # Resize image maintaining aspect ratio
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Center the image on the white background
        paste_x = (passport_size[0] - new_width) // 2
        paste_y = (passport_size[1] - new_height) // 2
        
        # Paste the resized image onto the white background
        background.paste(img, (paste_x, paste_y))
        
        # Save the final image
        background.save(output_path, 'JPEG', quality=95, dpi=(300, 300))
        
        print(f"Passport photo saved to: {output_path}")
        print("Please verify that:")
        print("1. The head height is between 1 inch and 1-3/8 inches")
        print("2. Eyes are between 1-1/8 inches and 1-3/8 inches from the bottom")
        print("3. The face is centered and the background is pure white")

if __name__ == "__main__":
    try:
        input_file_path = input("Enter the path of the input file: ")
        output_file_path = f"{input_file_path.split(".jpg")[0]}_converted_output.jpg"

        if not os.path.exists(input_file_path):
            print(f"Error: Input file '{input_file_path}' not found")

        create_passport_photo(input_file_path, output_file_path)
    except Exception as e:
        print(f"Error processing image: {str(e)}")