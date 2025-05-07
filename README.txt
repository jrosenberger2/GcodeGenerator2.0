GcodeGenerator was built for my Honors Thesis, as an experiemnt into how natural language processing could be used to simplify 3D printing.

Use of Gcode GeneratorV2.1:

--You will need blender and Ultimaker Cura installed locally relative to GeneratorV2.1.py

--Dependencies can be installed by running install.py

--The application can be run by running run.py

--To use the generator pick the record or selection mode

	-For Record Mode:
		-Clicking the record button will immediately record 5 seconds of audio from your systems microphone
		-The app expects to hear x by x by x and a valid shape in the audio
		-The app will then start to attempt to parse the recorded audio, assuming it contains 3 numbers and a shape
		-The app will then generate a model, and then gcode which will be stored in the Output folder

	-For Selection Mode:
		-Simply select the shape you want, and then input a valid size (1-200 mm)
		-The app will then generate a model and then gcode from that model which will be stored in the Output folder
