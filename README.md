# quick-start
This is a quick-start example for using datmo over iris classification dataset

### Installation:

   Requirements: docker      
    
    $ pip install datmo


### Steps:

1. Clone this github [project](!https://github.com/datmo/quick-start.git),
   ```
   $ git clone https://github.com/datmo/quick-start.git
   ```   

2. Move into the project and initialize it and setup the environment using datmo CLI,
   ```
   $ cd quick-start
   $ # Initialize the project using datmo
   $ datmo init
   $ # Set the name and description for the project
   $ # Enter `y` to setup the environment
   $ # Select `cpu`, `data-analytics`, `py27` based on the questions being asked   
   ```   
      
3. Now, run your first experiment using the following command,
   ```
   $ datmo run 'python script.py'
   $ # check for your first run using ls command
   $ datmo ls
   ```
   
4. Now let's change the script for a new run,
   
   ```
   vi script.py
   ```
   Uncomment the following line in the script and remove the other config dictionary,
   ```
   # config = { "solver": "liblinear", "penalty": "l1" }   
   ```

5. Now that we have updated the script, let's run another experiment,
   ```
   $ datmo run 'python script.py'
   $ # check for your first run using ls command
   $ datmo ls
   ```

6. With two test being tracked, we can now rerun any of the previous run with reprocibility,
   ```
   $ # Select the earlier run-id to rerun the first experiment
   $ datmo rerun < run-id >
   ```
   
Now, in this quick-start example, you have run two experiments, which are tracked and have 
rerun one of these tracked experiment.

 
