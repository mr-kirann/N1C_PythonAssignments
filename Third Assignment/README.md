# Third Assignment: Personal Expense Tracker

This is a simple command-line Personal Expense Tracker application written in Python. It allows users to add, view, and delete expenses, as well as view the total expenses. All expense data is stored in a MongoDB database.

## Features
- Add new expenses with description, amount, and date
- View all recorded expenses
- View the total sum of expenses
- Delete expenses by their ID

## Requirements
- Python 3.7 or above
- MongoDB (running locally on `mongodb://localhost:27017/`)
- Python packages: `pymongo`, `bson`

## Setup Instructions

1. **Clone or download this repository** and navigate to the `Third Assignment` folder:
   ```sh
   cd "Third Assignment"
   ```

2. **Install dependencies** using the provided `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```

3. **Ensure MongoDB is running locally**
   - If you do not have MongoDB installed, [download and install MongoDB Community Edition](https://www.mongodb.com/try/download/community).
   - Start the MongoDB server on your machine (default port 27017).

4. **Run the application:**
   ```sh
   python thirdAssign.py
   ```

## Usage
Follow the on-screen menu to add, view, or delete expenses. Each expense is stored in a MongoDB collection called `thirdAssignDB` in the `ThirdAssign` database.

### Example
```
Personal Expense Tracker
1. Add New Expense
2. View All Expenses
3. View Total Expenses
4. Delete an Expense
5. Exit
```

## Notes
- Make sure MongoDB is running before starting the application.
    - **If MongoDB is not running, the application will not work and will fail to connect to the database.**
- All data will be stored locally in your MongoDB instance.
- **If you encounter an error related to `bson.codec_options` or similar, run the following commands to fix the issue:**
  ```sh
  pip uninstall -y bson && pip install --upgrade --force-reinstall pymongo
  
  pip uninstall -y bson
  
  pip install --upgrade --force-reinstall pymongo
  ```
  The `bson` module is included with `pymongo` and should not be installed separately.

## License
This project is for educational purposes.
