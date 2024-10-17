#! /bin/sh
#---------------------------------------------------------------------------

IMGDIR="$1"
CPRSUBDIR="with-copyright"
THUMBSUBDIR="thumbnails"

test -d "$IMGDIR" || { echo "Error: no '$IMGDIR' directory." ; exit 1 ; }

(
    cd "${IMGDIR}" || exit 1 ;
    mkdir "$CPRSUBDIR"    
    for file in Inria-*.jpg ; do
	echo ${file}
	alt_name=$(echo output_${file} | sed s/output_Inria-0504-/indo-french-seminar-wireless-6g-photo/g )
	#echo "with-copyright/${alt_name} ${alt_name} ${file}"
	test -e "with-copyright/output_$file" || test -e "with-copyright/${alt_name}" || convert "$file" -gravity SouthEast -pointsize 36 -fill white -undercolor black -annotate +20+20 "© Inria / Photo B. Fourrier" "${CPRSUBDIR}/output_$file"
    done
)

(
    cd "${IMGDIR}" || exit 1 ; pwd
    cd "${CPRSUBDIR}" || exit 1; pwd
    for file in output_*.jpg ; do
	echo "ren ${file}"
	mv "${file}" $(echo ${file} | sed s/output_Inria-0504-/indo-french-seminar-wireless-6g-photo/g )
    done
)


(
    cd "${IMGDIR}" || exit 1 ; pwd
    cd "${CPRSUBDIR}" || exit 1; pwd
    mkdir "${THUMBSUBDIR}"
    for file in indo-french*.jpg ; do
	echo "thumb ${file}"
	test -e "${THUMBSUBDIR}/thumb_$file" || convert "$file" -thumbnail 150 "${THUMBSUBDIR}/thumb_$file"
    done
)

#---------------------------------------------------------------------------

(
    cd "${IMGDIR}" || exit 1 ; pwd
    cd "${CPRSUBDIR}" || exit 1; pwd
# Create the HTML file
cat <<EOF > gallery.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photo Thumbnails</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .thumbnail {
            margin: 10px;
            display: inline-block;
        }
        .thumbnail img {
            border: 1px solid #ccc;
            padding: 5px;
            max-width: 150px;
        }
    </style>
</head>
<body>
    <h1>Photo Gallery</h1>
    <div class="gallery">
EOF

# Loop through each image and add the corresponding HTML thumbnail
for file in $(ls -r *.jpg) ; do
  echo "<div class='thumbnail'><a href='$file'><img src='thumbnails/thumb_$file' alt='$file'></a></div>" >> gallery.html
done

# Finish the HTML file
cat <<EOF >> gallery.html
    </div>
</body>
</html>
EOF
)

#---------------------------------------------------------------------------
