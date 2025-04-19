# Crear un archivo .ris con las normas solicitadas en formato APA
ris_content = """
TY  - BILL
TI  - Ley 590 de 2000. Por la cual se dictan disposiciones para promover el desarrollo de las micro, pequeñas y medianas empresas
AU  - Congreso de Colombia
PY  - 2000
UR  - https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=4561
ER  -

TY  - BILL
TI  - Ley 905 de 2004. Por la cual se modifica la Ley 590 de 2000
AU  - Congreso de Colombia
PY  - 2004
UR  - https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=14036
ER  -

TY  - BILL
TI  - Decreto 957 de 2019. Por el cual se reemplaza la clasificación de las microempresas, pequeñas y medianas empresas
AU  - Ministerio de Comercio, Industria y Turismo
PY  - 2019
UR  - https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=108340
ER  -

TY  - BILL
TI  - Ley 1429 de 2010. Ley de Formalización y Generación de Empleo
AU  - Congreso de Colombia
PY  - 2010
UR  - https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=41245
ER  -

TY  - BILL
TI  - Ley 1014 de 2006. Ley de Fomento al Emprendimiento
AU  - Congreso de Colombia
PY  - 2006
UR  - https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=19168
ER  -

TY  - BILL
TI  - Ley 2069 de 2020. Ley de Emprendimiento
AU  - Congreso de Colombia
PY  - 2020
UR  - https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=151620
ER  -

TY  - BILL
TI  - Ley 1314 de 2009. Por la cual se regulan los principios y normas de contabilidad e información financiera y de aseguramiento
AU  - Congreso de Colombia
PY  - 2009
UR  - https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=36874
ER  -
"""

# Guardar el contenido en un archivo .ris
file_path = "biblografia_normas.ris"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(ris_content)

file_path