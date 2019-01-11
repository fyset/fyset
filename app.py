from dotenv import load_dotenv

from src.create_app import create_app


# Load .env into os.environ for using out of app context
load_dotenv(override=True)
# Create app
app = create_app()

# Run with 'python app.py'
if __name__ == "__main__":
    app.run()
