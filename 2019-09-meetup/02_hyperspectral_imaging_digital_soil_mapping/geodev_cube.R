# podatke najdi na http://www.enmap.org/
# set working directory
setwd("/home/mazinga/Documents/Hiperspektralci/R/Doeberitzer/")

# nalaganje knjižnic
library(sp)
library(raster)
library(rgdal)
library(hyperSpec)
library(hsdar)

# uvoz
pot <- "/home/mazinga/Documents/Hiperspektralci/podataki/Doeberitzer/HyMap09/090820_Doeberitz_02_REFL_POL_Geo.bsq"
hiperspektralci <- brick(pot)

# raster brick lahko izrežemo na kose, ki so primerni za obdelavo ("koliko RAM-a, toliko muzike") 
# klip in izvoz
e <- extent(368413.10, 370719.59, 5820993.15, 5823339.29)
cropped <- crop(hiperspektralci, e)

## nalaganje valovnih dolzin iz metapodakov
imena_kanalov <-names(hiperspektralci)
izlocene_dolzine <- substring(imena_kanalov,2)
valovne_dolzine <-  c(as.numeric(unlist(izlocene_dolzine, use.names=FALSE)))

## iskanje kanalov najblozjih zeljenim valovnim dolzinam
isci_kanal <- function(x) {
  isci_kanal <- which.min(abs(valovne_dolzine  - x))
  return(isci_kanal)
}

R <- isci_kanal(680)
G <- isci_kanal(540)
B <- isci_kanal(470)
NIR <- isci_kanal(830)
SWIR <- isci_kanal(1610)
SWIR_2 <- isci_kanal(2200)

# sestavi barvno in lažno barvne kompozite
RGB <- stack(cropped)[[c(R,G,B)]]
Color_infrared <- stack(cropped)[[c(NIR,R,G)]]
Urban_false_color <- stack(cropped)[[c(SWIR_2,SWIR,R)]]
Agriculture_false_color <- stack(cropped)[[c(SWIR,NIR,B)]]
Soil_false_color <- stack(cropped)[[c(SWIR_2,R,B)]]
Land_water_delim <- stack(cropped)[[c(NIR,SWIR,R)]]

# pregled
par(mfrow=c(3,2)) 
plotRGB(RGB, r=3, g=2, b=1, stretch="lin", main="RGB")
plotRGB(Color_infrared, r=3, g=2, b=1, stretch="lin", main="RGB")
plotRGB(Urban_false_color, r=3, g=2, b=1, stretch="lin", main="RGB")
plotRGB(Agriculture_false_color, r=3, g=2, b=1, stretch="lin", main="RGB")
plotRGB(Soil_false_color, r=3, g=2, b=1, stretch="lin", main="RGB")
plotRGB(Land_water_delim, r=3, g=2, b=1, stretch="lin", main="RGB")

## Kauth & Thomasove transformacije
tasseled_cap_bt <- function(a, b, c, d, e, f) {
  tasseled_cap_bt <- 0.3037*a +0.2793*b+0.4743*c+0.5585*d+0.5082*e+0.1863*f
  return(tasseled_cap_bt)
}

tasseled_cap_veg <- function(a, b, c, d, e_2, f) {
  tasseled_cap_veg <- -0.2848*a -0.2435*b-0.5436*c+0.7243*d+0.7243*e_2+0.0840*f
  return(tasseled_cap_veg)
}


izloci_sloj <- function(x,y) {
  izloci_sloj <- raster(cropped, isci_kanal(mean(c(x, y))))
  return(izloci_sloj)
}

a <- izloci_sloj(450, 520)
b <- izloci_sloj(520, 600)
c <- izloci_sloj(630, 690)
d <- izloci_sloj(760, 900)
e <- izloci_sloj(1150, 1750)
e_2 <- izloci_sloj(1550, 1750)
f <- izloci_sloj(2080, 2350)

KT_BT <- tasseled_cap_bt(a, b, c, d, e, f)
KT_VEG <- tasseled_cap_veg(a, b, c, d, e_2, f)
par(mfrow=c(1,2)) 
plot(KT_BT, axes=FALSE)
plot(KT_VEG, axes=FALSE)

# pretvori podatke v speclib format
cropped_speclib <- speclib(cropped, valovne_dolzine)

# izzdelaj podatkovno kocko
cubePlot(cropped_speclib, r=NIR, g=R, b=G, ncol = 1, nrow = 1, sidecol = colorRamp(palette(heat.colors(100))))