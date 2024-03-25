# Public Lands

The USGS makes a nice dataset available that describes conserved lands all over the United States.  And it includes information on whether that land is accessible to the public. (In a legal sense, rather than accomodation sense). Obviously, there's no guarantee of correctness, but it is still a good clue for where you might decide to go wander.

Unfortunately, it isn't complete.  I noticed there are a ton of places in my state (Massachusetts) that don't show up for some reason.  Luckily, Massachusetts GIS has their own dataset, which includes these extra places.  And several other states do too.

I've started with New England, writing scripts to download these different datasets, try to extract and normalize the fields that matter to me, and a script to merge all of the information into a single file.

Again, none of these datasets are authoritative -- don't assume anything about their accuracy!