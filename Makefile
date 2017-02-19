all: run

run:
	nextflow run pipeline.nf -resume

run-fresh:
	nextflow run pipeline.nf

docker:
	nextflow run pipeline.nf -with-docker

clean:
	rm -rf work results/*
