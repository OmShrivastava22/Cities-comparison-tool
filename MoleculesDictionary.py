#!/usr/bin/env python
# coding: utf-8

# In[30]:


from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors


# In[26]:


# List of compound names
compound_names = [
    "water",
    "oxygen",
    "nitrogen",
    "carbon_dioxide",
    "carbon_monoxide",
    "methane",
    "ammonia",
    "hydrogen_sulfide",
    "hydrogen",
    "chlorine",
    "hydrogen_chloride",
    "hydrogen_bromide",
    "hydrogen_iodide",
    "nitric_oxide",
    "nitrogen_dioxide",
    "nitrous_oxide",
    "ozone",
    "sulfur_dioxide"
    "ethanol",
    "acetic_acid",
    "glucose",
    "benzene",
    "acetone",
    "formaldehyde",
    "toluene",
    "phenol",
    "chloroform",
    "acetonitrile",
    "glycerol",
    "lactic_acid",
    "citric_acid",
    "formic_acid",
    "ethyl_acetate",
    "urea",
    "caffeine"
    "glycine",
    "alanine",
    "valine",
    "leucine",
    "isoleucine",
    "serine",
    "threonine",
    "cysteine",
    "methionine",
    "phenylalanine",
    "tyrosine",
    "tryptophan",
    "asparagine",
    "glutamine",
    "aspartic_acid",
    "glutamic_acid",
    "lysine",
    "arginine",
    "histidine",
    "proline"
]

# Corresponding SMILES strings (must be in same order)
smiles_strings = [
    "O",               # water
    "O=O",             # oxygen
    "N#N",             # nitrogen
    "O=C=O",           # carbon_dioxide
    "C#O",             # carbon_monoxide
    "C",               # methane
    "N",               # ammonia
    "S",               # hydrogen_sulfide
    "[H][H]",          # hydrogen
    "ClCl",            # chlorine
    "[H]Cl",           # hydrogen_chloride
    "[H]Br",           # hydrogen_bromide
    "[H]I",            # hydrogen_iodide
    "[N+]=[O-]",       # nitric_oxide
    "O=N(=O)[O-]",     # nitrogen_dioxide (approx NO3⁻)
    "N#[N+]O",         # nitrous_oxide
    "O=O=O",           # ozone
    "O=S=O"            # sulfur_dioxide
     "CCO",
    "CC(=O)O",
    "C(C1C(C(C(C(O1)O)O)O)O)O",
    "c1ccccc1",
    "CC(=O)C",
    "C=O",
    "Cc1ccccc1",
    "c1ccc(cc1)O",
    "ClC(Cl)Cl",
    "CC#N",
    "C(C(CO)O)O",
    "CC(C(=O)O)O",
    "C(C(=O)O)C(CC(=O)O)(C(=O)O)O",
    "C(=O)O",
    "CCOC(=O)C",
    "C(=O)(N)N",
    "Cn1cnc2c1c(=O)n(c(=O)n2C)C"
    "NCC(=O)O",                         # glycine
    "CC(C(=O)O)N",                      # alanine
    "CC(C)C(C(=O)O)N",                  # valine
    "CC(C)CC(C(=O)O)N",                 # leucine
    "CC(C)C(C(=O)O)N",                  # isoleucine
    "C(C(C(=O)O)N)O",                   # serine
    "CC(C(C(=O)O)N)O",                  # threonine
    "C(C(C(=O)O)N)S",                   # cysteine
    "CSCC(C(=O)O)N",                    # methionine
    "c1ccccc1CC(C(=O)O)N",              # phenylalanine
    "c1ccc(cc1O)CC(C(=O)O)N",           # tyrosine
    "c1cc2c(cc1)[nH]c2CC(C(=O)O)N",     # tryptophan
    "NC(CC(=O)O)C(=O)N",                # asparagine
    "NC(CCC(=O)O)C(=O)N",               # glutamine
    "CC(C(=O)O)C(=O)O",                 # aspartic_acid
    "CCC(C(=O)O)C(=O)O",                # glutamic_acid
    "CCCC(C(=O)O)N",                    # lysine
    "C(C[C@H](N)C(=O)O)CN=C(N)N",       # arginine
    "C1=CN=CN1CC(C(=O)O)N",             # histidine
    "C1CC(NC1)C(=O)O" 
]


# In[32]:


# Ask user for molecule name
user_input = input("Enter compound name(in single word like carbon_dioxide): ").strip().lower()

# Try to find and draw it
if user_input in compound_names:
    index = compound_names.index(user_input)
    mol = Chem.MolFromSmiles(smiles_strings[index])
    img= Draw.MolToImage(mol)
    print("Number of atoms:", mol.GetNumAtoms())
    mw=Descriptors.MolWt(mol)
    print(f"molecular weight:{mw} g/mol")
    for atom in mol.GetAtoms():
        print(atom.GetSymbol())   
    img.show()
else:
    print("Compound not found. Available options are:")
    print(compound_names)


# In[ ]:




