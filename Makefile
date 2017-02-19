all: run

run:
	nextflow run main.nf -resume

run-fresh:
	nextflow run main.nf

run-docker:
	nextflow run main.nf -with-docker

refresh-dag-image:
	rm -f flowchart.png
	nextflow run main.nf -with-dag flowchart.png

clean:
	rm -rf work results/*
