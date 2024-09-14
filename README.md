# **Barcode-Based Product Sale System**

This project scans barcodes using a camera, retrieves product information from a text file, and manages sales transactions. It provides the user with total price calculation, the amount of money received, and change to be returned. All transaction data is saved in a file.

## **Features**

- Barcode reading with a camera
- Fetching product information and prices from a text file
- Audible alert (sound file is played) after the product is scanned
- Change calculation based on the amount received from the customer
- Saving sales information in a `.txt` file

## **Installation**

### **Required Libraries**

The following libraries are required for the project to work smoothly:

```bash
pip install opencv-python
pip install pyzbar
pip install pygame
```

You can install them by running the commands above in your terminal.

### **File Structure**

The project uses the following file structure:

- **`urunler.txt`**: Contains product information and prices. Each line in the file includes the product name and barcode-price information in the following format:
  
  ```text
  ProductName Barcode:Price
  ```

  Example:

  ```text
  Apple 1234567890123:5.50
  Banana 9876543210987:10.00
  ```

- **`a.txt`**: Stores sales information after each transaction.
- **`a.mp3`**: The audio file played when a barcode is scanned (can be a beep or any other sound).

## **How It Works**

1. **Camera Connection**: When the program starts, the camera is opened, and it begins scanning barcodes.
2. **Product Scanning**: Once a product's barcode is scanned, its information and price are fetched from the `urunler.txt` file.
3. **Sound Playback**: A sound is played after the product is scanned.
4. **Total Price Calculation**: The total price of the scanned products is displayed on the screen.
5. **Change Calculation**: The user enters the amount of money received from the customer, and the change to be returned is automatically calculated.
6. **Saving Sales Information**: All transaction details are saved to the `a.txt` file.

## **Running the Code**

To run the code, use the following command in any Python environment or terminal:

```bash
python a.py
```

**Note**: Ensure that a camera is connected to your computer for barcode scanning.

## **Configuration**

- The path to the sound file is set in the **`ses_dosyasi`** variable. To use a custom sound file, modify the file path in the code.
- Product information is stored in **`urunler.txt`**. You can update the product name, barcode, and price in this file.
- The camera number is set by **`cap = cv2.VideoCapture(0)`**. If you're using a different camera, adjust the **`0`** value.

## **Contributing**

To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with detailed comments about your changes.
