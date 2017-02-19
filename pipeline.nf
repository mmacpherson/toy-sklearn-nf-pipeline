#!/usr/bin/env nextflow

def srcDir = baseDir + '/src'
def resultsDir = baseDir + '/results'


params.url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
params.out = "$resultsDir/summary.txt"
params.scales = ['unscaled', 'scaled', 'robust']
params.engines = ['ols', 'elasticnet']


process download_and_unpack {
    input:
    val params.url

    output:
    file dataset_text

    """
    curl -L "${params.url}" > dataset_text
    """
}

process process_dataset {
    input:
    file dataset_text

    output:
    file dataset into dataset_model, dataset_report

    """
    python $srcDir/process_dataset.py dataset_text dataset
    """
}

process build_model {
    input:
    file dataset_model
    each scale from params.scales
    each engine from params.engines

    output:
    file model

    "python $srcDir/build_model.py dataset $scale $engine model"

}

process summarize {
    input:
    file dataset_report
    file "models*" from model.toList()

    output:
    file summary

    "python $srcDir/report.py dataset models* > summary"
}

summary.collectFile(name: params.out)