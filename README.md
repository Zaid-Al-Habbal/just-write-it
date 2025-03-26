# Just Write It

## Features
-

## Prerequisites
Before building just-write-it, ensure you have the following installed on your system:

- python >= 10.0v
- git

## Setup for local development
1. Clone the repository:
   ```sh
   git clone https://github.com/Zaid-Al-Habbal/just-write-it.git
   cd just-write-it 
   ```
   
2. Set up virtual environment:
    ```sh
    python -m venv .venv/
    source venv/bin/activate
    ```
3. Install Dependencies:
   ```sh
    pip install -r requirements.txt
   ```
4. Run postgres container:
    ```sh
   docker run --name=blog_db -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=blog -d -p 5432:5432 postgres
    ```
5. Migrate Database:
    ```sh
    python manage.py migrate
    ```
7. Run server:
   ```sh
   python manage.py runserver

   
## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request detailing your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy exploring Cham City Center in 3D!

