# WorldQuant-IQC2024

This project is designed to automatically submit our alpha and use "Grid Search" to help find the best configuration settings for the alpha.

## Instructions

1. **Place Your Alpha:**
   - Put your alpha code in `alphas/{alpha_name}/code.txt`.

2. **Set Up Configurations:**
   - Define the configurations you want to search in `configs/select_settings.py`. The program will explore all combinations you set.

3. **Environment Settings:**
   - Fill in the settings in `.env.example` and rename the file to `.env`.

4. **Run the Program:**
   - Execute the following command:

     ```bash
     python main.py --alpha_name {alpha_name}
     ```
