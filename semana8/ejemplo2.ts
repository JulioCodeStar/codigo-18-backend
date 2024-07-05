
function manufacture(gifts: string[], materials: string) {
    const giftsManufactured: string[] = [];
  
    for (let gift of gifts) {
      let isPosible: boolean = true;
  
      for (let character of gift) {
        if (materials.split("").includes(character)) {
          isPosible = true;
        } else {
          isPosible = false;
          break;
        }
      }
  
      if (isPosible) {
        giftsManufactured.push(gift);
      }
    }
  
    return giftsManufactured;
  }
  
  const gifts = ["tren", "oso", "pelota"];
  const materials = "tronesa";
  console.log(manufacture(gifts, materials));