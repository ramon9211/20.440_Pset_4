# 20.440 Problemset 4: Build a repository for your project
### author:           Rajib Mondal
### Project partner:  Eddie Irvine

**Purpose: This repository provides a script to run a Python 3.8 PCA analysis on single-cell sequencing data from a Tuberculosis BCG-vaccine study on rhesus macaques published by Darrah et al.. It shall tell you in a strucutred way how to run this preliminary code.**

## Content
1. Project overview
2. Folder structure
3. Data
4. Run code
    - packages needed
    - run code
6. Citations

## Project overview
**Note: This section is motivating our project and provides context. If you just want to run the code, you can skip it.**

Mycobacterium tuberculosis (Mtb), the causative agent of tuberculosis (TB), was responsible for the death of an estimated 1.4 million people in 20191. While a licensed TB vaccine does exist in the form of Bacille Calmette-Guérin (BCG), BCG does no2t effectively prevent adult pulmonary TB2. As such, novel vaccination strategies are urgently needed to curb the ongoing TB epidemic. 
The development of an effective TB vaccine has been hampered by a poor understanding of protective immunity to Mtb. While CD4 T cells play a critical role in controlling Mtb infection3, efforts to generate vaccines that primarily exploit T cell immunity to drive protection have been met with limited success. Nevertheless, promising signals of vaccine efficacy have begun to emerge in several non-human primate (NHP) studies. 
Specifically, while the standard is to administer BCG through the intradermal (ID) route, intravenous (IV) administration of BCG has been shown to drive a 100,000-fold reduction in Mtb burden as compared to standard ID BCG following Mtb challenge in rhesus macaques4. Concomitant with their enhanced protection, IV BCG vaccinated macaques exhibited quantitatively higher CD4 and CD8 T cell counts in the lungs compared to standard ID BCG vaccinated animals4. Further, single cell RNA-seq (scRNAseq) analysis revealed that T cells in the bronchoalveolar lavage (BAL) of IV BCG immunized animals were enriched in memory T cell functionality, as well as in several genes associated with protection against Mtb4. 
While this original study demonstrated that IV BCG vaccination quantitatively and qualitatively enhances lung-localized T cell immunity, these data do not define the phenotypic effect of IV BCG vaccination on other lung-localized immune cell populations which represent plausible contributors to vaccine-induced protection. Thus, here we seek to test the hypothesis that IV BCG vaccination drives phenotypic changes in the lung-localized immune response beyond T cell immunity, which may underlie protection. Specifically, leveraging scRNAseq data derived from the BAL of animals that received either no vaccination, ID BCG vaccination, or IV BCG vaccination from the original study, we will identify potential transcriptional signals of protective immunity present in various -- non-T cell -- immune cell populations. This work will be systematically executed in the following specific aims:

**Aim 1** Define the transcriptional profiles in lung-localized macrophages that uniquely evolve following IV BCG vaccination. Macrophages represent a primary cellular niche for Mtb during infection3. Furthermore, macrophages exhibit significant heterogeneity in their capacity to control Mtb replication5. Thus, in aim 1, we will test the hypothesis that IV BCG vaccination drives macrophages phenotypically poised to restrict Mtb. 

**Aim 2** Define the transcriptional profiles in lung-localized B cells that uniquely evolve following IV BCG vaccination. B cells are required for the optimal control of Mtb in mice6, hinting at a role for humoral immunity in protection against TB. Moreover, B cell numbers and antibody titers significantly increased in the BAL following IV BCG vaccination4, suggesting the robust induction of local humoral immunity by IV BCG immunization. In aim 2, we will test the hypothesis that in addition to the increase in magnitude of B cell responses, IV BCG instantiates unique B cell subpopulations in the lung following vaccination.

**Aim 3** Define the transcriptional profiles in lung-localized Natural Killer (NK) cells that uniquely evolve following IV BCG vaccination. Cytotoxic NK cells are enriched in individuals with latent TB -- a group able to maintain control of bacterial replication -- pointing to a potential functional role for this cell type in Mtb control7. Like B cells, NK cell numbers were increased in the BAL following IV BCG vaccination, yet the phenotypic state of these cells was not assessed4. Thus, in aim 3, we will test the hypothesis that IV BCG immunization uniquely drives the induction of cytotoxic NK cells in the lungs.


## Folder structure
Code: proves all python scripts
Results: location to save generated Figures

## Data
Please download the data folder from here:
https://drive.google.com/drive/folders/1bmsc-dkCZcWmv4pQV-WLtqKuWIGtZKvu?usp=sharing

After cloning the repository add the data to the parental folder of your repository.

The folder Data contains two subfolders: a) GSE139598_Week13_Stimulated.Cells.UMI.collapsed.CHUNKED and b) Original.
a) contains the actual single sequencing data
b) contains meta data to label the cells

## Run code
**a) Packages**

Code is run on Python 3.8

Following packages are needed:
- numpy
- sklearn
- seaborn
- os

You can install these packages using pip or conda.

**b) Run script**
1. Clone repository to your desired location on your machine
2. Save data from google drive to the parental folder of you repository.
3. Open terminal
4. Navigate to folder "Code"
5. type into your command line: python PCA_single_cell_analaysis.py

The Figure will pop up on your screen and is automatically saved in the results folder. If you would like to change the name of your saved Figure open the script and change the variable "resultName" as desired.

## Citation
1.Darrah, P. A. et al. Prevention of tuberculosis in macaques after intravenous BCG immunization. Nature 577, 95–102 (2020).

