def create_codon_dict(file_path):
    my_dict = {}
    file = open(file_path, "r")
    rows = file.readlines()
    file.close()
    for row in rows:
      cell = row.strip().split('\t') 
      my_dict[cell[0]] = cell[2]
    return my_dict

