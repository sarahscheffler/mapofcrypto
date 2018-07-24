# Map of Crypto Links and Objects

### Latest changes
* 2018/07/23. SS.  Removing objects we already have and links that we aren't
  using.
* 2018/05/15. SS.  Tidying up this document for sending an email.
* 2018/05/11. SS.  Initial commit.  Added initial list of protocols to include, 
  link types, categories, etc.

### TODO
* Conditional on receiving feedback and conducting any major changes:
    * Assign UIDs to everything
    * Provide an easy way to (1) contribute and (2) verify an object or link
    * Start defining links

## Link types
* "X is a type of Y (all X are Y)".
    * Example: A "Trapdoor permutation" is a type of "one-way permutation"
    * "X can be used as a building block (along with Z1 and Z2) for Y".  To do
      this, use multiple sources in the `source_dest` list.
* "∃X implies ∃Y"
    * Example: "Trapdoor permutations" can be used to build "IND-CCA-secure PKE"
      [Yao82]

## Entities
### Primitives
* ~~PRGs~~
* PRFs
    * Constrained PRFs
    * Strong
    * Weak
    * PRPs
        * Strong
        * Weak
* OWFs
    * ~~Strong~~
        * TODO: Existing OWF node should be StrongOWF.
    * Weak
    * OWPs
    * Trapdoor OWPs
    * Universal OWF
    * Hard core predicates
* KE
* CRHF (not sure where to put?)
* $t$-wise indep fns
* Universal HF
* KA
    * 2-KA
    * k-KA

### Types of Schemes
* PKE
    * IND-CCA (and NM-CCA)
    * IND-CPA
    * Others?
* Signature Scheme
    * EU-CMA
* Symmetric key encryption
    * IND-CCA
    * IND-CPA
* Message Authentication Codes
    * EU-CMA
* FE
    * IBE
    * ABE
* HE
* FHE
* Commitments

### Obfuscation stuff?  I have no idea what to do with this TBH.
* VBB
* VGB
* iO

## Future Map Ideas

### Map of knowledge
* PoK
* IP
* ZK
    * Constant round
    * NIZK
    * SNARKs
* WI

### Map of MPC
* SS
* GC
* OT [Actually, we might just want to have an entire MPC map]
    * 2-SH-OT
    * k-SH-OT





