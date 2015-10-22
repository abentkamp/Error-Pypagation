from sympy.physics.unitsystems.dimensions import Dimension
from units import BaseUnit,DerivedUnit

length=Dimension(length=1)
time=Dimension(time=1)
mass=Dimension(mass=1)
current=Dimension(current=1)
temperature=Dimension(temperature=1)
amount=Dimension(amount=1)
luminosity=Dimension(luminosity=1)

system={}
system["m"]=	BaseUnit("m",length)
system["s"]=	BaseUnit("s",time)
system["kg"]=	BaseUnit("kg",mass)
system["A"]=	BaseUnit("A",current)
system["K"]=	BaseUnit("K",temperature)
system["mol"]=	BaseUnit("mol",amount)
system["cd"]=	BaseUnit("cd",luminosity)

system["Hz"]=	DerivedUnit("Hz","1/s",system,standard=False)
system["N"]=	DerivedUnit("N","kg*m/s**2",system)
system["Pa"]=	DerivedUnit("Pa","N/m**2",system)
system["J"]=	DerivedUnit("J","N*m",system)
system["W"]=	DerivedUnit("W","J/s",system)
system["C"]=	DerivedUnit("C","A*s",system)
system["V"]=	DerivedUnit("V","W/A",system)
system["F"]=	DerivedUnit("F","C/V",system)
system["Ohm"]=	DerivedUnit("Ohm","V/A",system)
system["ohm"]=	DerivedUnit("ohm","V/A",system,standard=False)
system["S"]=	DerivedUnit("S","1/Ohm",system,standard=False)
system["Wb"]=	DerivedUnit("Wb","V*s",system)
system["T"]=	DerivedUnit("T","Wb/m**2",system)
system["H"]=	DerivedUnit("H","Wb/A",system)

system["min"]=	DerivedUnit("min","60*s",system,standard=False)
system["h"]=	DerivedUnit("h","3600*s",system,standard=False)
system["d"]=	DerivedUnit("d","24*3600*s",system,standard=False)

def extend_by_prefixes(unit,system):
	for prefix,factor in [("p",1e-12),("n",1e-9),("mu",1e-6),("m",1e-3),("c",1e-2),("d",1e-1),("da",1e1),("h",1e2),("k",1e3),("M",1e6),("G",1e9),("T",1e12)]:
		system[prefix+unit.name]=DerivedUnit(prefix+unit.name,unit*factor,system,standard=False)


systemCopy=system.copy()
for name in systemCopy:
	if not name=="kg":
		extend_by_prefixes(system[name],system)

system["pg"]=	DerivedUnit("pg","1e-15*kg",system,standard=False)
system["ng"]=	DerivedUnit("ng","1e-12*kg",system,standard=False)
system["mug"]=	DerivedUnit("mug","1e-9*kg",system,standard=False)
system["mg"]=	DerivedUnit("mg","1e-6*kg",system,standard=False)
system["cg"]=	DerivedUnit("cg","1e-5*kg",system,standard=False)
system["dg"]=	DerivedUnit("dg","1e-4*kg",system,standard=False)
system["g"]=	DerivedUnit("g","1e-3*kg",system,standard=False)
system["dag"]=	DerivedUnit("dag","1e-2*kg",system,standard=False)
system["hg"]=	DerivedUnit("hg","1e-1*kg",system,standard=False)
system["Mg"]=	DerivedUnit("Mg","1e3*kg",system,standard=False)
system["Gg"]=	DerivedUnit("Gg","1e6*kg",system,standard=False)
system["Tg"]=	DerivedUnit("Tg","1e9*kg",system,standard=False)
