const randomWord = () => {
    let wordList = [
        "marriageproof",
        "minionette",
        "unlichened",
        "electrocardiographic",
        "hippophagy",
        "polyphore",
        "debellate",
        "zyga",
        "antedonin",
        "hirudinean",
        "foremastman",
        "metapolitics",
        "bianisidine",
        "gros",
        "superindifferent",
        "collar",
        "maculose",
        "unphysically",
        "narrowish",
        "Bartonia",
        "inadherent",
        "arbitrary",
        "forefeelingly",
        "palame",
        "vina",
        "northwestward"
        ]
    let idx = Math.floor(Math.random() * wordList.length) + 1
    return wordList[idx]
}
export default randomWord;