

**`chef_guide.md`**
```markdown
# Chef Guide

- Recipes, cookbooks, and resources
- Example:
```ruby
package 'nginx' do
  action :install
end
service 'nginx' do
  action [:enable, :start]
end
