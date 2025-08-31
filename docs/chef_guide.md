

**`chef_guide.md`**

<img width="2048" height="2048" alt="Gemini_Generated_Image_s54r2ss54r2ss54r" src="https://github.com/user-attachments/assets/daaaba50-932e-4521-881d-d2ca9e948d86" />

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
