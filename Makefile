default: report.pdf
.PHONY: deafult

Subject_1_data.csv Subject_2_data.csv: datadownloader.py
	python3 datadownloader.py

TimeComparison.pdf: TimeComparison.py Subject_1_data.csv Subject_2_data.csv
	python3 TimeComparison.py

Acf_activities.pdf: Acf_activities.py Subject_1_data.csv Subject_2_data.csv
	python3 Acf_activities.py

report.pdf: TimeComparison.pdf Acf_activities.pdf
        pdflatex report.tex
        biber report
        pdflatex report.tex
        pdflatex report.tex

clean:
        rm *.pdf *.csv *.aux *.log *.blg *.bbl *.bcf *.run.xml

.PHONY: clean
