# This file is part of MorphoDiTa <http://github.com/ufal/morphodita/>.
#
# Copyright 2015 Institute of Formal and Applied Linguistics, Faculty of
# Mathematics and Physics, Charles University in Prague, Czech Republic.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys

from ufal.morphodita import *

tagger = Tagger.load("czech-morfflex-pdt-161115-derinet20.tagger")
converter = TagsetConverter.newStripLemmaIdConverter(tagger.getMorpho())
derivator = tagger.getMorpho().getDerivator()

def lemmatize(text):
    forms = Forms()
    lemmas = TaggedLemmas()
    derivated_lemma = DerivatedLemma()
    tokens = TokenRanges()
    tokenizer = tagger.newTokenizer()
    if tokenizer is None:
        sys.stderr.write("No tokenizer is defined for the supplied model!")
        sys.exit(1)

    # Tag
    output = []
    tokenizer.setText(text)
    while tokenizer.nextSentence(forms, tokens):
        tagger.tag(forms, lemmas)
        for i in range(len(lemmas)):
            while derivator.parent(lemmas[i].lemma, derivated_lemma):
                lemmas[i].lemma = derivated_lemma.lemma
            converter.convert(lemmas[i])
            output.append({"lemma": lemmas[i].lemma, "form": forms[i], "start_index": tokens[i].start, "end_index": tokens[i].start + tokens[i].length})
            for key in ["lemma", "form"]:
                if output[-1][key] == "–":
                    output[-1][key] = "-"

    return output
