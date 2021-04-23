# Go Platforms Actions

Github Actions to generate cross platforms matrix for golang build

## Usage

```yaml
jobs:
  job1:
    outputs:
      matrix: ${{ steps.platforms.outputs.matrix }}
    steps:
    - id: platforms
      uses: t-actions/go-platforms@master
      with:
        # Platforms to build
        # Default is all platforms by $(go tool dist list)
        platforms: ''
  job2:
    need: job1
    strategy:
      matrix: ${{ fromJson(needs.job1.outputs.matrix) }}
```

## Output Format

matrix
```json
{
  "include": [
    {
      "goos": null,
      "goarch": null,
      "goarm": null
    }
  ]
}
```