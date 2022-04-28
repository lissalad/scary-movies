from app import app, db
import os

port=int(os.environ.get('PORT', 3000))

if __name__ == "__main__":
  app.run(debug=True, port=port)
