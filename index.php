<?php


$python = `python v4.py`;
//echo ($python);


$myfile = fopen("output.txt", "r") or die("Unable to open file!");
//echo fread($myfile,filesize("output.txt"));
while(!feof($myfile)) {
  echo fgets($myfile) . "<br>";
}
fclose($myfile);

?>