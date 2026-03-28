FROM mysql:8.0

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root
# Expose the default MySQL port
EXPOSE 3306