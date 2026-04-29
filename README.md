# Hudl Login Test Automation Project

This project is a Playwright test automation framework built with Python and pytest to test the Hudl login flow.

## Tech Stack

- Python
- Playwright
- pytest
- python-dotenv

## Test Coverage

The test suite covers:

- Login page loads successfully
- User can log in with valid credentials
- Invalid credentials show an error message
- Empty password validation
- Forgot password flow navigates to the email confirmation page

## Project Structure

```
hudl_login_project/
├── pages/
│   └── login_page.py
├── tests/
│   └── test_login.py
├── utils/
│   └── config.py
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup Instructions

Clone the repository:

```
git clone https://github.com/BrooklenBlack/hudl_login_project.git
cd hudl_login_project
```

Create a virtual environment:

```
python -m venv .venv
```

Activate the virtual environment (Windows):

```
.venv\Scripts\Activate.ps1
```

Install dependencies:

```
python -m pip install -r requirements.txt
```

Install Playwright browsers:

```
python -m playwright install
```

## Environment Variables

Create a `.env` file in the root of the project using `.env.example` as a guide:

```
HUDL_EMAIL=
HUDL_PASSWORD=
HUDL_BASE_URL=https://www.hudl.com
```

Add your Hudl test account credentials to this file.  
The `.env` file should **not** be committed to GitHub.

## Running Tests

Run all tests:

```
python -m pytest
```

Run tests with the browser visible:

```
python -m pytest --headed --slowmo 500
```

## Running in Visual Studio Code (Optional)

Open the project folder in Visual Studio Code.

Make sure the Python extension is installed.

Select the virtual environment:
- Press `Ctrl + Shift + P`
- Search for `Python: Select Interpreter`
- Choose the `.venv` interpreter

Open a terminal in VS Code and run:

```
python -m pytest
```

## Notes

- Credentials are handled through environment variables and are excluded from version control.
- This project uses a Page Object Model (`LoginPage`) to keep tests clean and maintainable.
