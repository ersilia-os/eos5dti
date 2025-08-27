# Acinetobacter baumannii activity prediction

Acinetobacter baumannii activity prediction based on phenotypic ChEMBL data. Each column corresponds to a specific bioactivity dataset derived from ChEMBL, encompassing multiple assays and binarization cut-offs. The global consensus score summarizes the probability of being active. Model developed by Ersilia.

This model was incorporated on 2025-06-13.Last packaged on 2025-08-27.

## Information
### Identifiers
- **Ersilia Identifier:** `eos5dti`
- **Slug:** `chembl-abaumannii`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`
- **Target Organism:** `Acinetobacter baumannii`
- **Tags:** `A.baumannii`, `Antimicrobial activity`, `ChEMBL`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `26`
- **Output Consistency:** `Fixed`
- **Interpretation:** The higher the probabilities and the global consensus scores, the more likely this compound is active against Acinetobacter baumannii

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| 0_consensus_score | float | high | Consensus score among datasets |
| 1_assay_chembl4296188_inhibition_percentage_activity_percentile_10_organism_1 | float | high | Predicted probability of being active according to task 1_assay_chembl4296188_inhibition_percentage_activity_percentile_10_organism_1 |
| 1_assay_chembl4296188_inhibition_percentage_activity_percentile_1_organism_1 | float | high | Predicted probability of being active according to task 1_assay_chembl4296188_inhibition_percentage_activity_percentile_1_organism_1 |
| 1_assay_chembl4296188_inhibition_percentage_activity_percentile_50_organism_2 | float | high | Predicted probability of being active according to task 1_assay_chembl4296188_inhibition_percentage_activity_percentile_50_organism_2 |
| 1_assay_chembl4296188_inhibition_percentage_activity_percentile_5_organism_1 | float | high | Predicted probability of being active according to task 1_assay_chembl4296188_inhibition_percentage_activity_percentile_5_organism_1 |
| 1_assay_chembl4296188_mic_pchembl_percentile_10_organism_3 | float | high | Predicted probability of being active according to task 1_assay_chembl4296188_mic_pchembl_percentile_10_organism_3 |
| 1_assay_chembl4296188_mic_pchembl_percentile_1_organism_1 | float | high | Predicted probability of being active according to task 1_assay_chembl4296188_mic_pchembl_percentile_1_organism_1 |
| 1_assay_chembl4296188_mic_pchembl_percentile_5_organism_1 | float | high | Predicted probability of being active according to task 1_assay_chembl4296188_mic_pchembl_percentile_5_organism_1 |
| 1_assay_chembl4296188_mic_pchembl_value_5_organism_1 | float | high | Predicted probability of being active according to task 1_assay_chembl4296188_mic_pchembl_value_5_organism_1 |
| 1_assay_chembl4296193_inhibition_percentage_activity_percentile_10_organism_3 | float | high | Predicted probability of being active according to task 1_assay_chembl4296193_inhibition_percentage_activity_percentile_10_organism_3 |

_10 of 26 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos5dti](https://hub.docker.com/r/ersiliaos/eos5dti)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5dti.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5dti.zip)

### Resource Consumption
- **Model Size (Mb):** `473`
- **Environment Size (Mb):** `731`
- **Image Size (Mb):** `2145.61`

**Computational Performance (seconds):**
- 10 inputs: `33.06`
- 100 inputs: `22.49`
- 10000 inputs: `335`

### References
- **Source Code**: [https://github.com/ersilia-os/chembl-antimicrobial-models](https://github.com/ersilia-os/chembl-antimicrobial-models)
- **Publication**: [https://ersilia.io/](https://ersilia.io/)
- **Publication Type:** `Other`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos5dti
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos5dti
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
