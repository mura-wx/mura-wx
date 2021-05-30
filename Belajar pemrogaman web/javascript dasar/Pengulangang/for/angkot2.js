var noAngkot = 1;
var angkotBeroperasi = 4;
var jmlAngkot = 10;

while(noAngkot <= angkotBeroperasi) {
	console.log("Angkot No. " + noAngkot + " beroperasi dengan baik.");
noAngkot++;	
}

for (noAngkot = angkotBeroperasi + 1; noAngkot <= jmlAngkot ; noAngkot++) {
	console.log("Angkot No. " + noAngkot + " sedang tidak berperasi.");
}