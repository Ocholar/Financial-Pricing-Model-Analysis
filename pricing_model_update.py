import pandas as pd
import numpy as np

# Define file paths
input_file = "/home/ubuntu/upload/_Candidate_Name_-_2024_Pricing_Model_-_MW.xlsx"
output_file = "2024_Pricing_Model_Completed.xlsx"

# --- Assumptions and Constants from PDF ---
FX_RATE_DEC_2023 = 1700.0
REPAYMENT_RATE = 0.98
INVENTORY_SHRINK = 0.005
TARGET_MARGIN_PERCENT = 0.25

# --- Data Loading ---
xls = pd.ExcelFile(input_file)
df_pricing_model = xls.parse('Pricing Model', header=None)
df_input_sheet = xls.parse('Input Sheet', header=None)
df_bundle_config = xls.parse('Bundle Configuration', header=None)
df_2023_adoption = xls.parse('2023 Adoption', header=None)

# --- Helper Functions ---
def get_bundle_cogs(bundle_name, df_config):
    cogs_mwk = 0
    if bundle_name == '0.2 Acre Maize bundle':
        cogs_mwk = pd.to_numeric(df_config.iloc[3:6, 7], errors='coerce').sum()
    elif bundle_name == '1.5 Acre Maize bundle':
        cogs_mwk = pd.to_numeric(df_config.iloc[7:13, 7], errors='coerce').sum()
    elif bundle_name == '1 Acre Maize bundle':
        cogs_mwk = pd.to_numeric(df_config.iloc[14:17, 7], errors='coerce').sum()
    elif bundle_name == '1/2 Acre Maize bundle':
        cogs_mwk = pd.to_numeric(df_config.iloc[18:21, 7], errors='coerce').sum()
    else:
        cogs_row = df_config[df_config.iloc[:, 3] == bundle_name]
        if not cogs_row.empty:
            cogs_mwk = pd.to_numeric(cogs_row.iloc[0, 7], errors='coerce')
        else:
            cogs_row = df_config[df_config.iloc[:, 2] == bundle_name]
            if not cogs_row.empty:
                cogs_mwk = pd.to_numeric(cogs_row.iloc[0, 7], errors='coerce')
            else:
                mismatches = {
                    'Legume; Tikolore; 2 KG Bag [Stock]': 'Legume; Soya beans Tikolore; 2 KG Bag [Stock]',
                    'Legume; Soya beans Tikolore; 1KG [Stock]': 'Legume; Soya beans Tikolore; 1KG [Stock]',
                    'Legume; Soya beans Tikolore; 5KG[Stock]': 'Legume; Soya beans Tikolore; 5KG[Stock]',
                    'Legume; Soya beans Tikolore; 10KG[Stock]': 'Legume; Soya beans Tikolore; 10KG[Stock]',
                    'Legume; Soya beans Tikolore; 20KG[Stock]': 'Legume; Soya beans Tikolore; 20KG[Stock]',
                }
                if bundle_name in mismatches:
                    cogs_row = df_config[df_config.iloc[:, 3] == mismatches[bundle_name]]
                    if not cogs_row.empty:
                        cogs_mwk = pd.to_numeric(cogs_row.iloc[0, 7], errors='coerce')

    return np.nan_to_num(cogs_mwk)

def calculate_selling_price(cogs_mwk, target_margin_percent, repayment_rate, inventory_shrink):
    if cogs_mwk == 0:
        return 0
    revenue_needed = cogs_mwk / (1 - target_margin_percent)
    selling_price = revenue_needed / (repayment_rate * (1 - inventory_shrink))
    return round(selling_price)

# --- Data Processing ---
df_pricing_model.iloc[13, 2] = FX_RATE_DEC_2023
df_pricing_model.iloc[13, 3] = FX_RATE_DEC_2023
df_pricing_model.iloc[13, 4] = FX_RATE_DEC_2023

start_row_index = 5
end_row_index = len(df_input_sheet)

for i in range(start_row_index, end_row_index):
    bundle_name = df_input_sheet.iloc[i, 2]
    if pd.isna(bundle_name) or bundle_name in ['Maize Bundle - Standard', 'Maize Bundle - Reduced Urea', 'Top up Products']:
        continue
    cogs_mwk = get_bundle_cogs(bundle_name, df_bundle_config)
    if cogs_mwk != 0:
        df_input_sheet.iloc[i, 5] = cogs_mwk
        df_input_sheet.iloc[i, 9] = cogs_mwk
        selling_price = calculate_selling_price(cogs_mwk, TARGET_MARGIN_PERCENT, REPAYMENT_RATE, INVENTORY_SHRINK)
        df_input_sheet.iloc[i, 6] = selling_price
        df_input_sheet.iloc[i, 10] = selling_price

total_farmers_2023 = df_2023_adoption.iloc[0, 4]
df_2023_adoption.columns = df_2023_adoption.iloc[1]
df_2023_adoption = df_2023_adoption[2:].reset_index(drop=True)
df_2023_adoption['Adoption %'] = pd.to_numeric(df_2023_adoption['Total Adoption'], errors='coerce').fillna(0) / total_farmers_2023

southern_sites = df_pricing_model.iloc[2, 2]
southern_farmers_per_site = df_pricing_model.iloc[3, 2]
central_sites = df_pricing_model.iloc[2, 3]
central_farmers_per_site = df_pricing_model.iloc[3, 3]
southern_farmers_2024 = southern_sites * southern_farmers_per_site
central_farmers_2024 = central_sites * central_farmers_per_site
total_farmers_2024 = southern_farmers_2024 + central_farmers_2024
df_pricing_model.iloc[4, 4] = total_farmers_2024

for i in range(start_row_index, end_row_index):
    bundle_name = df_input_sheet.iloc[i, 2]
    if pd.isna(bundle_name) or bundle_name in ['Maize Bundle - Standard', 'Maize Bundle - Reduced Urea', 'Top up Products']:
        continue
    adoption_row = df_2023_adoption[df_2023_adoption['Bundle'] == bundle_name]
    if not adoption_row.empty:
        adoption_percent = adoption_row['Adoption %'].iloc[0]
        df_input_sheet.iloc[i, 3] = adoption_percent
        df_input_sheet.iloc[i, 4] = round(adoption_percent * southern_farmers_2024)
        df_input_sheet.iloc[i, 7] = adoption_percent
        df_input_sheet.iloc[i, 8] = round(adoption_percent * central_farmers_2024)
        df_input_sheet.iloc[i, 15] = df_input_sheet.iloc[i, 4] + df_input_sheet.iloc[i, 8]
        df_input_sheet.iloc[i, 16] = adoption_percent
        df_input_sheet.iloc[i, 17] = df_input_sheet.iloc[i, 15]

for i in range(start_row_index, end_row_index):
    bundle_name = df_input_sheet.iloc[i, 2]
    if pd.isna(bundle_name) or bundle_name in ['Maize Bundle - Standard', 'Maize Bundle - Reduced Urea', 'Top up Products']:
        continue
    southern_units = pd.to_numeric(df_input_sheet.iloc[i, 4], errors='coerce')
    southern_selling_price = pd.to_numeric(df_input_sheet.iloc[i, 6], errors='coerce')
    southern_cogs = pd.to_numeric(df_input_sheet.iloc[i, 5], errors='coerce')
    central_units = pd.to_numeric(df_input_sheet.iloc[i, 8], errors='coerce')
    central_selling_price = pd.to_numeric(df_input_sheet.iloc[i, 10], errors='coerce')
    central_cogs = pd.to_numeric(df_input_sheet.iloc[i, 9], errors='coerce')
    
    southern_units = np.nan_to_num(southern_units)
    southern_selling_price = np.nan_to_num(southern_selling_price)
    southern_cogs = np.nan_to_num(southern_cogs)
    central_units = np.nan_to_num(central_units)
    central_selling_price = np.nan_to_num(central_selling_price)
    central_cogs = np.nan_to_num(central_cogs)

    total_revenue_mwk = (southern_units * southern_selling_price) + (central_units * central_selling_price)
    total_cogs_mwk = (southern_units * southern_cogs) + (central_units * central_cogs)
    total_revenue_usd = total_revenue_mwk / FX_RATE_DEC_2023
    total_cogs_usd = total_cogs_mwk / FX_RATE_DEC_2023
    total_margin_usd = total_revenue_usd - total_cogs_usd
    
    df_input_sheet.iloc[i, 18] = total_revenue_usd
    df_input_sheet.iloc[i, 19] = total_cogs_usd
    df_input_sheet.iloc[i, 20] = total_margin_usd
    if total_revenue_usd != 0:
        df_input_sheet.iloc[i, 21] = total_margin_usd / total_revenue_usd
    else:
        df_input_sheet.iloc[i, 21] = 0

total_revenue_usd_core = pd.to_numeric(df_input_sheet.iloc[start_row_index:end_row_index, 18], errors='coerce').sum()
total_cogs_usd_core = pd.to_numeric(df_input_sheet.iloc[start_row_index:end_row_index, 19], errors='coerce').sum()
southern_ratio = southern_farmers_2024 / total_farmers_2024
central_ratio = central_farmers_2024 / total_farmers_2024

df_pricing_model.iloc[5, 2] = total_revenue_usd_core * southern_ratio
df_pricing_model.iloc[5, 3] = total_revenue_usd_core * central_ratio
df_pricing_model.iloc[5, 4] = total_revenue_usd_core
df_pricing_model.iloc[6, 2] = total_cogs_usd_core * southern_ratio
df_pricing_model.iloc[6, 3] = total_cogs_usd_core * central_ratio
df_pricing_model.iloc[6, 4] = total_cogs_usd_core
df_pricing_model.iloc[9, 2] = total_cogs_usd_core * southern_ratio
df_pricing_model.iloc[9, 3] = total_cogs_usd_core * central_ratio
df_pricing_model.iloc[9, 4] = total_cogs_usd_core

total_margin_usd_core = total_revenue_usd_core - total_cogs_usd_core
df_pricing_model.iloc[10, 2] = total_margin_usd_core * southern_ratio
df_pricing_model.iloc[10, 3] = total_margin_usd_core * central_ratio
df_pricing_model.iloc[10, 4] = total_margin_usd_core

if df_pricing_model.iloc[5, 2] != 0:
    df_pricing_model.iloc[11, 2] = df_pricing_model.iloc[10, 2] / df_pricing_model.iloc[5, 2]
else:
    df_pricing_model.iloc[11, 2] = 0
if df_pricing_model.iloc[5, 3] != 0:
    df_pricing_model.iloc[11, 3] = df_pricing_model.iloc[10, 3] / df_pricing_model.iloc[5, 3]
else:
    df_pricing_model.iloc[11, 3] = 0
if total_revenue_usd_core != 0:
    df_pricing_model.iloc[11, 4] = total_margin_usd_core / total_revenue_usd_core
else:
    df_pricing_model.iloc[11, 4] = 0

if southern_farmers_2024 != 0:
    df_pricing_model.iloc[12, 2] = df_pricing_model.iloc[5, 2] / southern_farmers_2024
else:
    df_pricing_model.iloc[12, 2] = 0
if central_farmers_2024 != 0:
    df_pricing_model.iloc[12, 3] = df_pricing_model.iloc[5, 3] / central_farmers_2024
else:
    df_pricing_model.iloc[12, 3] = 0
if total_farmers_2024 != 0:
    df_pricing_model.iloc[12, 4] = total_revenue_usd_core / total_farmers_2024
else:
    df_pricing_model.iloc[12, 4] = 0

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_pricing_model.to_excel(writer, sheet_name='Pricing Model', index=False, header=False)
    df_input_sheet.to_excel(writer, sheet_name='Input Sheet', index=False, header=False)
    xls.parse('>> Start Here').to_excel(writer, sheet_name='>> Start Here', index=False, header=False)
    xls.parse('Bundle Configuration').to_excel(writer, sheet_name='Bundle Configuration', index=False, header=False)
    xls.parse('Site Economics').to_excel(writer, sheet_name='Site Economics', index=False, header=False)
    xls.parse('2023 Adoption').to_excel(writer, sheet_name='2023 Adoption', index=False, header=False)

print(f"Successfully updated and saved the file to {output_file}")
