
Pharmacy Management System – README
===================================

Contact Information:
--------------------
Author: Rachel Fitzgerald
Email: rfitzgerald3@mail.pima.edu

Project Overview:
-----------------
This is a basic Pharmacy Management System written in Python. It allows users to:

- Add, update, and remove medicines from inventory
- Handle customer sales
- Calculate total bills
- Validate inputs (e.g., no negative prices)
- Optionally save/load inventory data using files

How to Run the Program:
-----------------------
1. Install Python 3.x (recommended: Python 3.10 or higher)
2. Open your terminal or command prompt
3. Navigate to the project folder
4. Run the program using:

   python main.py

Dependencies:
-------------
- This project uses only built-in Python modules (no external packages required).
- Optional: `tkinter` for GUI features (if implemented)

Features:
---------
- Object-Oriented design with classes (`Medicine`, `Inventory`)
- Input validation (positive numbers, valid expiry date format)
- Simple recursion (e.g., search or report generation) [not yet implemented]
- Optional file-based data persistence (CSV or TXT) [not yet implemented]
- Optional GUI using Tkinter (may be included if time allows)

File Manifest:
--------------
- main.py                        # Main program file
- Pharmacy Management System Workflow.pdf   # Program flowchart
- Revised_Plan.pdf or .docx      # Revised project plan
- README.txt                     # This documentation file

Known Limitations:
------------------
- File saving is basic and may not be included
- GUI features are optional and may be incomplete
- No user authentication or multi-user support

Troubleshooting:
----------------
- Ensure you are using Python 3.8+
- If the program fails to start, check for syntax errors or missing files
- If using file save/load, ensure `inventory.csv` is in the same directory
