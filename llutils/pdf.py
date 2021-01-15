class pdf:
    def __init__(self):
        pass

    @classmethod
    def merge(self, output_name = "merged.pdf", files = None, folder = None, folder_excl = None):
        """
        function to merge multiple pdf files into 1 \n
        if both a folder and files are provided, both will be in the merge, with the specified files first
        *---------------------------------------------*
        output_name:    the file name of the merged pdf \n
        files:          path to files to add to the merge \n
        folder:         a folder containing 1 or more pdf files to merge \n
        folder_excl:    files in the given folder to exclude from the merge (relative path)
        """
        print("pdf")
        # from matplotlib.backends.backend_pdf import PdfPages
        # import matplotlib.pyplot as plt

        # with PdfPages("test/test.pdf") as pdf:
        #     pdf.savefig("test/test.pdf")
        #     'test_files/Dag14_slides_kausalitet.pdf'
            

