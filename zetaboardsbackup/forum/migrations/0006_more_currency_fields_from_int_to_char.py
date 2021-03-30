# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'CurrencyTable.to_currency'
        db.alter_column('library_currencytable', 'to_currency', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'CurrencyTable.from_currency'
        db.alter_column('library_currencytable', 'from_currency', self.gf('django.db.models.fields.CharField')(max_length=3))


    def backwards(self, orm):
        
        # Changing field 'CurrencyTable.to_currency'
        db.alter_column('library_currencytable', 'to_currency', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CurrencyTable.from_currency'
        db.alter_column('library_currencytable', 'from_currency', self.gf('django.db.models.fields.IntegerField')())


    models = {
        'library.book': {
            'Meta': {'ordering': "['isbn']", 'object_name': 'Book'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'library.currencytable': {
            'Meta': {'ordering': "['from_currency', 'to_currency']", 'object_name': 'CurrencyTable'},
            'from_currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'to_currency': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'library.price': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Price'},
            '_converted_currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            '_converted_delivery': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            '_converted_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            '_converted_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            '_native_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Book']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'error': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'native_currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'native_delivery': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'native_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Shop']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'library.shop': {
            'Meta': {'ordering': "['-featured', 'name']", 'object_name': 'Shop'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'delivery': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['library']
