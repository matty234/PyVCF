import vcf

vcf_reader = vcf.Reader(open('vcf/test/example-4.0.vcf', 'r'))
for record in vcf_reader:
    print(record)