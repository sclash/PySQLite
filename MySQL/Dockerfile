FROM mysql:8.0

# Use the official MySQL image as the base image

# Set the MySQL root password (change 'password' to your desired password)
ENV MYSQL_ROOT_PASSWORD=password

# Copy the initialization script to the container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port
EXPOSE 3306