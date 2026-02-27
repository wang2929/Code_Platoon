exports.isCharacterMatch = function(string1, string2) {
    let modified_string1 = string1.replaceAll(" ", "").toUpperCase();
    let modified_string2 = string2.replaceAll(" ", "").toUpperCase();
    if (modified_string1.length != modified_string2.length) {
        return false;
    }
    for (let c of modified_string1) {
        let idx = modified_string2.indexOf(c);
        if (idx < 0) {
            return false;
        }
        modified_string2 = modified_string2.replace(c, "");
    }
    return true;
};
