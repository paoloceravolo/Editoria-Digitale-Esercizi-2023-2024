import pandocfilters as pf
import datetime

def replace_date(key, value, format, meta):
	if key == "Header" and value[0] == 4:
		text = pf.stringify(value[2])
		current_date = datetime.datetime.now().strftime("%d/%m/%Y")  # Get the current date in the desired format
		updated_text = text.replace("#### Aggiornato il", "#### Aggiornato il " + current_date)
		return pf.Header(value[0], [value[1], value[2], pf.Str(updated_text)])

if __name__ == "__main__":
	pf.toJSONFilter(replace_date)