# Use an official base image
# Chat GPT suggested this when I inputted an error message from using a different base image
# This is a good minimimal installer for Conda
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /cf593_doxy

# Copy the current directory contents into the container
COPY . /cf593_doxy

# new conda environment created called RC_environment.yml
RUN conda env create -f RC_environment.yml

# Run the command with the following command
CMD ["conda", "run", "-n", "RC_environment", "python", "main.py", "input.txt"]
