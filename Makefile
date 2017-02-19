all: run

run:
	nextflow run pipeline.nf -resume

run-fresh:
	nextflow run pipeline.nf

run-docker:
	nextflow run pipeline.nf -with-docker

refresh-dag-image:
	rm -f flowchart.png
	nextflow run pipeline.nf -with-dag flowchart.png

clean:
	rm -rf work results/*
