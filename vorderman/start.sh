#!/bin/sh

echo "Running db init"
python initDB.py
echo "Running API server"
python app.py
