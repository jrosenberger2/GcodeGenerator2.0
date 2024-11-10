#Using curaEngine to slice given stl file in cmd
import subprocess
import streamlit as st
import trimesh
import re
import whisper

def generate(shape, x,y,z):
    product = x + "x" + y + "x" + z + " " + shape
    st.write('Generating Gcode for a ', product)
    product = ''.join(product.split())
    #product
    filename = product + '.gcode'
    subprocess.run(["Blender 4.2\\blender", "--background", "--python", "Shapes\\"+shape+".py", x, y, z])
    st.write("Done!")
    slice(shape, filename)


def slice(shape, outputName):
    st.write("Slicing 3D Model")

    #Use trimesh to convert glb to stl
    mesh = trimesh.load("Models\\"+shape+".glb", force='mesh')
    mesh.export("Models\\"+shape+".stl")#open("C:\\Users\\jared\\Downloads\\OutputShift.stl", 'w'), )

    subprocess.run(["UltiMaker Cura 5.8.1\\CuraEngine", "slice", "-v",
                "-j", "UltiMaker Cura 5.8.1\\share\\cura\\resources\\definitions\\fdmprinter.def.json",
                "-j","UltiMaker Cura 5.8.1\\share\\cura\\resources\\definitions\\fdmextruder.def.json",
                "-j", "UltiMaker Cura 5.8.1\\share\\cura\\resources\\definitions\\creality_profile_update.def.json",
                "-o", "Output\\"+outputName, "-l", "Models\\"+shape+".stl"])
    st.write("Done!")
    #"C:\Program Files\UltiMaker Cura 5.8.1\share\cura\resources\quality\creality\base\base_0.4_PLA_standard.inst.cfg"
    #"C:\Program Files\UltiMaker Cura 5.8.1\share\cura\resources\materials\generic_pla_175.xml.fdm_material"
    #"C:\Program Files\UltiMaker Cura 5.8.1\share\cura\resources\materials\generic_pla.xml.fdm_material"

#whisperParse parse the audio file output.wave for size & shape requirements for the gcode
def whisperParse():
    st.write("Listing to recording...")
    model = whisper.load_model("tiny.en")
    result = model.transcribe("output.wave")
    hyp = result["text"]
    st.write("You said: " + hyp)
    size_pattern = '\d.+\d.+\d'
    shape_pattern = '(cube|cylinder|cone|Sphere)'
    size_match = re.search(size_pattern, hyp)
    shape_match = re.search(shape_pattern, hyp)

    shape = shape_match.group().capitalize()
    size_list = re.split('\s*[a-zA-Z]+\s*', size_match.group())
    x = size_list[0]
    y = size_list[1]
    z = size_list[2]
    
    generate(shape, x, y, z)
#slice()


##
#Streamlit App interface
##
st.title('Gcode Generator V2')
#st.markdown('Type or use voice to text to enter a 3D shape and it\'s dimensions in the text box.')
mode =st.selectbox('Select the generation mode you\'d like to use.', ['Voice to Text', 'Selection'])
if mode == 'Voice to Text':
    recordButton = st.button('Record 5 Seconds of Voice')
    if recordButton:
        st.write("Recording...")
        subprocess.run(['python', 'Record.py'])
        whisperParse()
else:
    shape = str(st.selectbox('Select the shape you would like to generate', ['Cube', 'Cylinder', 'Cone', 'Sphere']))
    length = str(st.number_input('Input the length in mm', 1, 200))
    width = str(st.number_input('Input the width in mm', 1, 200))
    height = str(st.number_input('Input the height in mm', 1, 200))
    
    enterClicked = st.button('Generate Gcode')
    if enterClicked:
        generate(shape, length, width, height)