rule ExampleMalware {
    meta:
        description = "Example YARA rule for testing"
        author = "Jyot Bhavsar"
    strings:
        $magic = { 4D 5A }  // MZ header for PE files
    condition:
        $magic at 0
}
